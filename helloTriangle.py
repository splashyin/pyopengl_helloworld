import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
from ctypes import *
from OpenGL.arrays import vbo as glvbo
import numpy as np


# =================================================
# Shaders
# =================================================

VERTEX_SHADER="""
#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0f);
}
"""

FRAGMENT_SHADER="""
#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
}
"""

# =================================================
# Globals
# =================================================

VERTICES=glvbo.VBO(
    np.array([0.0,  0.5, 0.0, 
               0.5, -0.5, 0.0,
              -0.5, -0.5, 0.0], dtype='float32')
)

# =================================================

def main():
    # Initialize the library
    if not glfw.init():
        return
        
    # Configure GL Context
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Apple specific
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
   
    # Create a windowed mode window
    window = glfw.create_window(800, 600, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)

    glBufferData(GL_ARRAY_BUFFER, len(VERTICES) *
                 VERTICES.itemsize, VERTICES, GL_STATIC_DRAW)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # Compile shaders
    compiledVertexShader = compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
    compiledFragmentShader = compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

    if glGetShaderiv(compiledVertexShader, GL_COMPILE_STATUS) != GL_TRUE:
        raise Exception("vertex shader did not compile")
        
    if glGetShaderiv(compiledFragmentShader, GL_COMPILE_STATUS) != GL_TRUE:
        raise Exception("fragment shader did not compile")

    shader = compileProgram(compiledVertexShader, compiledFragmentShader)

    if glGetProgramiv(shader, GL_LINK_STATUS) != GL_TRUE:
        raise Exception("program did not link")

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClearColor(0.2, 0.3, 0.3, 1.0)
        
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )        # Swap front and back buffers
        
        glUseProgram(shader)
        glBindVertexArray(VAO)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

# =================================================

if __name__ == "__main__":
    main()

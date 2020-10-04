import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

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

SHADER_PROGGRAM=None

def compileShaderPrograms():
    global SHADER_PROGGRAM
    compiledVertexShader = compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
    compiledFragmentShader = compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    SHADER_PROGRAM = compileProgram(compiledVertexShader, compiledFragmentShader)

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

    # Compile shaders
    compileShaderPrograms()

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

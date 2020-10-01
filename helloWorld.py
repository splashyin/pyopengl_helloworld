import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import compileShader, compileProgram


vertices = {
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0,  0.5, 0.0
}

vertexShader="""
#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}
"""

fragmentShader="""
#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
} 
"""

shaderProgram=None
VBO=None
VAO=None


def compileShaderPrograms():
    global shaderProgram
    compiledVertexShader = compileShader(vertexShader, GL_VERTEX_SHADER)
    compiledFragmentShader = compileShader(fragmentShader, GL_FRAGMENT_SHADER)
    shaderProgram = compileProgram(compiledVertexShader, compiledFragmentShader)


def display():
    global VAO
    # Clear the color and depth buffer
    glClearColor(0.2, 0.3, 0.3, 1.0)
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

    # render stuff here
    glUseProgram(shaderProgram)
    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Copy the off-screen buffer to the screen
    glutSwapBuffers()


glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
glutInitContextVersion(3, 2)
glutInitContextProfile(GLUT_CORE_PROFILE)
# Init
glutInit(sys.argv)



# Create a double-buffer RGBA window.   (Single-buffering is possible.
# So is creating an index-mode window.)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_3_2_CORE_PROFILE)

# Create a window, setting its title
glutCreateWindow('interactive')

compileShaderPrograms()

glGenVertexArrays(1, VAO)
glGenBuffers(1, VBO)
glBindVertexArray(VAO)

glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.__sizeof__(), vertices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 8)
glEnableVertexAttribArray(0)
glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)

# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)

# Run the GLUT main loop until the user closes the window.
glutMainLoop()

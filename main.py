from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

angle = 0  # Rotation angle
object_x = -1.5  # Object initial position
speed = 0.02  # Movement speed

def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    # Light properties
    light_pos = [1, 2, 1, 1]  # Light position
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])  # White light

def draw_sphere():
    glPushMatrix()
    glTranslatef(object_x, 0, 0)  # Move object
    glRotatef(angle, 0, 1, 0)  # Rotate object
    glColor3f(1, 0, 0)  # Red color
    glutSolidSphere(0.3, 50, 50)  # Sphere
    glPopMatrix()

def draw_shadow():
    global object_x
    glPushMatrix()
    glTranslatef(object_x, -0.48, 0)  # Shadow position
    glColor4f(0, 0, 0, 0.5)  # Transparent black for shadow
    glScalef(1, 0.1, 1)  # Flatten shadow
    glutSolidSphere(0.3, 50, 50)  # Shadow shape
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 1, 3, 0, 0, 0, 0, 1, 0)
    
    glColor3f(0.3, 0.3, 0.3)  # Gray floor
    glBegin(GL_QUADS)
    glVertex3f(-2, -0.5, -1)
    glVertex3f(2, -0.5, -1)
    glVertex3f(2, -0.5, 1)
    glVertex3f(-2, -0.5, 1)
    glEnd()
    
    draw_shadow()
    draw_sphere()
    
    glutSwapBuffers()

def update(value):
    global angle, object_x, speed
    angle += 2  # Rotate
    object_x += speed  # Move object
    
    if object_x > 1.5 or object_x < -1.5:
        speed = -speed  # Reverse direction
    
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 FPS

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 10)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Moving Sphere with Shadows")
    
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

main()

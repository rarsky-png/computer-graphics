#version 400 core

// Vertex shader de repasse .
// Nao transforma a geometria , apenas a encaminha .
// Usado por 03 _triangulo .py , 04 _quadrado .py e 05 _quadrado_diagonal .py.

layout(location = 0) in vec4 vPosition;
layout(location = 1) in vec4 vColors;

out vec4 v2fcolor;

void main(){
    gl_Position = vPosition;
    v2fcolor = vColors;
}
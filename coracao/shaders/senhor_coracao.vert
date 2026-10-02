#version 400 core

// Vertex shader de repasse .
// Nao transforma a geometria , apenas a encaminha .
// Usado por 03 _triangulo .py , 04 _quadrado .py e 05 _quadrado_diagonal .py.

layout(location = 0) in vec4 vPosition;

uniform float u_escala;
uniform vec2 u_deslocamento;
uniform vec4 u_cor;

out vec4 v2fcolor;

void main(){
    gl_Position = vec4(vPosition.xy * u_escala + u_deslocamento, vPosition.zw);
    
    v2fcolor = u_cor;
}
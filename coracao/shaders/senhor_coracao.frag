#version 400 core

// Fragment shader de repasse .
// Devolve a cor ja interpolada pelo rasterizador .

in vec4 v2fcolor;
uniform float u_atenuacao;
out vec4 outfragcolor;

void main(){
    outfragcolor = vec4(v2fcolor.rgb * u_atenuacao, v2fcolor.a);
}
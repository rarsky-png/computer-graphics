"""
Quadrado com EBO: quatro vertices, dois triangulos, seis indices.
MCCC007-23 - Computacao Grafica - UFABC

Executar: python 05_quadrado_diagonal.py      Sair: ESC ou fechar a janela

Teclas: ESPACO alterna a diagonal, D alterna o fundo, ESC sao
"""
import sys
from pathlib import Path

import glfw
import moderngl
import numpy as np

SHADERS = Path(__file__).parent / "shaders"

VERTICES = np.array([
    -0.5, -0.5, 0.0, 1.0,   1.0, 0.0, 0.0, 1.0,   # v0 vermelho
     0.5, -0.5, 0.0, 1.0,   0.0, 1.0, 0.0, 1.0,   # v1 verde
     0.5,  0.5, 0.0, 1.0,   0.0, 0.0, 1.0, 1.0,   # v2 azul
    -0.5,  0.5, 0.0, 1.0,   1.0, 1.0, 0.0, 1.0,   # v3 amarelo
], dtype='f4')

DIAGONAL_02 = np.array([0, 1, 2, 2, 3, 0], dtype='u4')
DIAGONAL_13 = np.array([0, 1, 3, 1, 2, 3], dtype='u4')

BRANCO = (1.0, 1.0, 1.0, 1.0)
PRETO = (0.0, 0.0, 0.0, 0.0)


def erro_glfw(codigo, descricao):
    """sem este callcank a razao real de uma falha do GLFW é descartada"""
    print(f"GLFW [{codigo}]: {descricao}", file=sys.stderr)


glfw.set_error_callback(erro_glfw)   # antes de glfw.init(), de proposito

if not glfw.init():
    sys.exit("FALHA: glfw nao inicializou")

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)


janela = glfw.create_window(600, 600, "Troca de diagonal", None, None)
if not janela:
    glfw.terminate()
    sys.exit("FALHA: nao foi possivel criar a janela")

glfw.make_context_current(janela)
glfw.swap_interval(1)
ctx = moderngl.create_context()

prog = ctx.program(
    vertex_shader=(SHADERS / "basico.vert").read_text(encoding="utf-8"),
    fragment_shader=(SHADERS / "basico.frag").read_text(encoding="utf-8"),
)



# Dois triangulos pela diagonal 0-2. Os indices sao inteiros SEM sinal:
# o arranjo de elementos do OpenGL e GL_UNSIGNED_INT.

vbo = ctx.buffer(VERTICES.tobytes())
ebo = ctx.buffer(DIAGONAL_02.tobytes())

vao = ctx.vertex_array(
    prog, [(vbo, '4f 4f', 'vPosition', 'vColors')], index_buffer=ebo
)

#o estado que os ecemplos anteriorres nao tinham 

diagonal_alternativa = False
modo_noite = False

def tecla(window, key, scancode, action, mods):
    global diagonal_alternativa, modo_noite
    if action != glfw.PRESS:
        return
    
    if key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)
    elif key == glfw.KEY_D:
        modo_noite = not modo_noite
    elif key == glfw.KEY_SPACE:
        diagonal_alternativa = not diagonal_alternativa
        
        novos = DIAGONAL_13 if diagonal_alternativa else DIAGONAL_02
        ebo.write(novos.tobytes())
        
glfw.set_key_callback(janela, tecla)
    

while not glfw.window_should_close(janela):
    ctx.clear(*(PRETO if modo_noite else BRANCO))
    vao.render(moderngl.TRIANGLES)
    glfw.swap_buffers(janela)
    glfw.poll_events()

for recurso in (vao, ebo, vbo, prog):
        recurso.release()

glfw.terminate()
print("Execucao finalizada.")

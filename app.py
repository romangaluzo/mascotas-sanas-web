from flask import Flask, render_template

app = Flask(__name__)

# Lista de cursos con TUS LINKS de afiliado (no modificados)
# IMPORTANTE: los precios son de referencia. Verificalos abriendo cada link
# en una ventana de incógnito y comparalos con el checkout de Hotmart.
cursos = [
    {
        "titulo": "Mascotas Sanas (Alimentación)",
        "precio": "97.00 USD",
        "img": "foto1.jpg",
        "link": "https://go.hotmart.com/V105110069K?dp=1",
        "descripcion": "Masterclass de alimentación natural casera para perros y gatos: cómo armar dietas, elegir alimentos y evaluar el alimento comercial. Incluye certificado."
    },
    {
        "titulo": "Primeros Auxilios Caninos",
        "precio": "49.99 USD",
        "img": "foto2.jpg",
        "link": "https://go.hotmart.com/C63284199M?dp=1",
        "descripcion": "Aprendé a armar un botiquín, reconocer urgencias y dar los primeros cuidados a tu perro antes de llegar al veterinario. Incluye certificado."
    },
    {
        "titulo": "Peluquería Perros PRO",
        "precio": "49.99 USD",
        "img": "foto3.jpg",
        "link": "https://go.hotmart.com/V105110074P?dp=1",
        "descripcion": "Aprendé desde cero baño, cepillado, desenredado y corte con máquina y tijera, según el tipo de pelo y la raza."
    },
    {
        "titulo": "Pastelería Canina y Felina",
        "precio": "69.99 USD",
        "img": "foto4.jpg",
        "link": "https://go.hotmart.com/X105090474W",
        "descripcion": "Aprendé a preparar snacks y tortas caseras para perros y gatos con ingredientes simples, y a leer las etiquetas del alimento comercial."
    },
    {
        "titulo": "Alimentación Especial",
        "precio": "10.00 USD",
        "img": "foto5.jpg",
        "link": "https://go.hotmart.com/N105116839I?dp=1",
        "descripcion": "E-book para armar dietas caseras personalizadas para perros con condiciones de salud especiales. Consultá siempre con tu veterinario."
    },
    {
        "titulo": "Embellecimiento Canino",
        "precio": "24.99 USD",
        "img": "foto6.jpg",
        "link": "https://go.hotmart.com/E105116847N",
        "descripcion": "Curso de una semana sobre cuidado del pelaje y la piel, higiene dental y técnicas de corte, con bonus de cuidado de uñas y patas."
    },
    {
        "titulo": "Recetas Anti-Inflamatorias",
        "precio": "12.99 USD",
        "img": "foto7.jpg",
        "link": "https://go.hotmart.com/M105116867K?dp=1",
        "descripcion": "E-book con 92 recetas naturales para perros y gatos. Es una guía educativa y no reemplaza el consejo de tu veterinario."
    },
    {
        "titulo": "Estilismo y Cortes",
        "precio": "20.00 USD",
        "img": "foto8.jpg",
        "link": "https://go.hotmart.com/U105116877L?dp=1",
        "descripcion": "Curso de peluquería canina: técnicas de corte, uso de herramientas y manejo de distintos tipos de pelaje y razas, con bonus."
    }
]

@app.route('/')
def home():
    return render_template('index.html', productos=cursos)

if __name__ == '__main__':
    # debug=False para que no quede expuesto el depurador si se publica con este comando
    app.run(debug=False)
from flask import Flask, render_template

app = Flask(__name__)

# Lista de cursos con TUS LINKS de afiliado actualizados
cursos = [
    {
        "titulo": "Mascotas Sanas (Alimentación)", 
        "precio": "97.00 USD", 
        "img": "foto1.jpg", 
        "link": "https://go.hotmart.com/V105110069K?dp=1", 
        "descripcion": "La guía definitiva de nutrición natural para que tus mascotas vivan más años."
    },
    {
        "titulo": "Primeros Auxilios Caninos", 
        "precio": "49.99 USD", 
        "img": "foto2.jpg", 
        "link": "https://go.hotmart.com/C63284199M?dp=1", 
        "descripcion": "No esperes a la emergencia. Aprendé las maniobras fundamentales para salvar vidas."
    },
    {
        "titulo": "Peluquería Perros PRO", 
        "precio": "49.99 USD", 
        "img": "foto3.jpg", 
        "link": "https://go.hotmart.com/V105110074P?dp=1", 
        "descripcion": "Aprendé cortes estéticos y cuidados higiénicos profesionales desde cero."
    },
    {
        "titulo": "Pastelería Canina y Felina", 
        "precio": "69.99 USD", 
        "img": "foto4.jpg", 
        "link": "https://go.hotmart.com/V105110074P?dp=1", 
        "descripcion": "Creá snacks y tortas saludables sin químicos. ¡A tus mascotas les va a encantar!"
    },
    {
        "titulo": "Alimentación Especial", 
        "precio": "10.00 USD", 
        "img": "foto5.jpg", 
        "link": "https://go.hotmart.com/V105110074P?dp=1", 
        "descripcion": "Guía especializada para perros con necesidades nutricionales específicas."
    },
    {
        "titulo": "Embellecimiento Canino", 
        "precio": "24.99 USD", 
        "img": "foto6.jpg", 
        "link": "https://go.hotmart.com/E105116847N", 
        "descripcion": "Salón de belleza en casa. Técnicas para que tus mascotas luzcan siempre radiantes."
    },
    {
        "titulo": "Recetas Anti-Inflamatorias", 
        "precio": "12.99 USD", 
        "img": "foto7.jpg", 
        "link": "https://go.hotmart.com/M105116867K?dp=1", 
        "descripcion": "Mejorá la salud de tu mascota con recetas naturales que reducen la inflamación."
    },
    {
        "titulo": "Estilismo y Cortes", 
        "precio": "20.00 USD", 
        "img": "foto8.jpg", 
        "link": "https://go.hotmart.com/U105116877L?dp=1", 
        "descripcion": "Curso enfocado en estilos modernos y cortes profesionales para diferentes razas."
    }
]

@app.route('/')
def home():
    return render_template('index.html', productos=cursos)

if __name__ == '__main__':
    app.run(debug=True)
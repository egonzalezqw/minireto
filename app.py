import streamlit as st

st.set_page_config(page_title="Mini Reto Bash", layout="centered")

st.title("🧪 Mini Reto – Bash Scripting")
st.subheader("Linux")

st.write("""
⏱️ Instrucciones:
- Lee cada script cuidadosamente
- Responde las preguntas
- Al final revisa tu puntuación
""")

score = 0

# =========================
# SCRIPT 1
# =========================
st.markdown("## 🧠 Script 1")

st.code("""
#!/bin/bash
echo "Inicio del sistema"
user=$(whoami)
echo "Usuario: $user"
""")

q1 = st.radio("1. ¿Qué hace `whoami`?", [
    "Muestra el sistema operativo",
    "Muestra el usuario actual",
    "Muestra archivos",
    "Muestra procesos"
])

if q1 == "Muestra el usuario actual":
    score += 1

q2 = st.radio("2. ¿Qué imprime primero el script?", [
    "Usuario",
    "Inicio del sistema",
    "Error",
    "Nada"
])

if q2 == "Inicio del sistema":
    score += 1


# =========================
# SCRIPT 2
# =========================
st.markdown("## 🧠 Script 2")

st.code("""
#!/bin/bash
for i in 1 2 3
do
  echo "Proceso $i"
done
""")

q3 = st.radio("3. ¿Cuántas veces se ejecuta el loop?", [
    "1",
    "2",
    "3",
    "4"
])

if q3 == "3":
    score += 1

q4 = st.radio("4. ¿Qué imprime el script?", [
    "Proceso 1 2 3 en una sola línea",
    "Proceso 1, 2, 3 en líneas separadas",
    "Error",
    "Nada"
])

if q4 == "Proceso 1, 2, 3 en líneas separadas":
    score += 1


# =========================
# SCRIPT 3 (ERROR DEBUGGING)
# =========================
st.markdown("## 🧠 Script 3 – Detecta el error")

st.code("""
#!/bin/bash
name = "Carlos"
echo "Hola $name"
""")

q5 = st.radio("5. ¿Cuál es el error?", [
    "Falta echo",
    "Espacios en asignación de variable",
    "Falta loop",
    "No hay error"
])

if q5 == "Espacios en asignación de variable":
    score += 1

q6 = st.text_input("6. Escribe la forma correcta de la variable:")

if q6.strip() == 'name="Carlos"' or q6.strip() == "name='Carlos'":
    score += 1


# =========================
# SCRIPT 4 (PIPE / ANALISIS)
# =========================
st.markdown("## 🧠 Script 4 – Pipes")

st.code("""
#!/bin/bash
ls /etc | grep conf
""")

q7 = st.radio("7. ¿Qué hace el pipe `|`?", [
    "Guarda archivos",
    "Conecta comandos",
    "Elimina archivos",
    "Copia archivos"
])

if q7 == "Conecta comandos":
    score += 1

q8 = st.radio("8. ¿Qué hace este comando final?", [
    "Busca archivos con extensión .conf",
    "Elimina archivos",
    "Crea archivos",
    "Ordena archivos"
])

if q8 == "Busca archivos con extensión .conf":
    score += 1


# =========================
# SCRIPT 5 (SALIDA SIMULADA)
# =========================
st.markdown("## 🧠 Script 5 – Salida")

st.code("""
#!/bin/bash
echo "A"
echo "B"
echo "C"
""")

q9 = st.radio("9. ¿Qué salida produce?", [
    "A B C en una línea",
    "A, B, C en líneas separadas",
    "Error",
    "Nada"
])

if q9 == "A, B, C en líneas separadas":
    score += 1


# =========================
# RETO FINAL
# =========================
st.markdown("## 🔥 Reto Final")

st.write("""
Crea mentalmente (no se ejecuta aquí) un script que:
- Muestre la fecha
- Muestre el usuario
- Liste archivos
""")

q10 = st.text_input("10. Escribe el comando para mostrar la fecha:")

if q10.strip() == "date":
    score += 1


# =========================
# RESULTADO
# =========================
st.markdown("---")

if st.button("📊 Ver resultados"):
    st.success(f"Puntuación final: {score} / 10")

    if score == 10:
        st.balloons()
        st.write("🔥 Excelente dominio del análisis de scripts")
    elif score >= 7:
        st.write("👍 Buen nivel")
    elif score >= 4:
        st.write("⚠️ Nivel básico, necesitas práctica")
    else:
        st.write("📚 Refuerzo urgente en Bash")

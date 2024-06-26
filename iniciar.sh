#!/bin/bash
#lsof -i:5000
# Verificar si el entorno virtual existe
if [ ! -f venv/bin/activate ]; then
    echo "No existe venv/"
    exit 1
fi
trap cerrar EXIT
function cerrar() {
  echo "Cerrando flask server"
  pkill -f "flask run --debug"

  echo "Cerrando python3 server"
  pkill -f "python3 -m http.server"
  gnome-terminal --tab -- bash -c "git restore data/; exec bash"
}

echo "Activando el entorno virtual..."
source venv/bin/activate

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "El entorno virtual no se activó correctamente."
    exit 1
else
    echo "Entorno virtual activado en: $VIRTUAL_ENV"
fi
# Iniciar el servidor backend Flask en segundo plano
echo "Iniciando el servidor backend Flask..."
cd backend/ && flask run --debug &

# Abrir una nueva pestaña de terminal
echo "Iniciando el servidor frontend..."
gnome-terminal --tab -- bash -c "cd frontend/ && python3 -m http.server; exec bash"

gnome-terminal --tab -- bash -c "code ."
wait

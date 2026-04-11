#!/bin/bash

echo "Actualizando repositorio..."
git pull origin main

echo "Ejecutando pipeline..."
python3 simulador_pipeline.py

echo "Proceso terminado."

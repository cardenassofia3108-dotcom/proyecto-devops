# #  Proyecto DevOps - AWS Academy

Este proyecto implementa una infraestructura automatizada en la nube utilizando **Amazon Web Services (AWS)**, enfocándose en la eficiencia, seguridad y observabilidad.

## Tecnologías Utilizadas
* **Cloud:** AWS (EC2, S3, IAM, CloudFormation).
* **Lenguajes:** Python (Boto3) y Bash Scripting.
* **Control de Versiones:** Git y GitHub.
* **Contenedores:** Docker (Dockerfile configurado).

##  Funcionalidades del Proyecto

### 1. Infraestructura como Código (IaC)
Se utilizó un template de **CloudFormation** (`template.yaml`) para desplegar de forma automática el bucket de S3 y la instancia EC2, asegurando que el entorno sea replicable.

### 2. Automatización con Python (Boto3)
El script `gestion_aws.py` interactúa directamente con el SDK de AWS para generar un reporte de recursos en tiempo real. 
> **Nota de Seguridad:** Se configuró un **IAM Role (LabInstanceProfile)** para permitir la comunicación segura entre la EC2 y los servicios de AWS sin exponer credenciales.

### 3. Automatización de Sistema (Bash + Cron)
Se implementó el script `limpieza_logs.sh` para el mantenimiento automático del servidor, programado mediante una tarea **Cron** para ejecutarse diariamente.

##  Cómo ejecutar el reporte
1. Entrar a la instancia EC2 vía SSH.
2. Ejecutar el script:
   ```bash
   python3 gestion_aws.pyproyecto-devops

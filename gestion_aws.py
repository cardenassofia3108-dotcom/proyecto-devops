import boto3
from datetime import datetime

def generar_reporte():
    session = boto3.Session(region_name='us-east-1')
    ec2 = session.client('ec2')
    s3 = session.client('s3')
    
    print("Obteniendo datos de AWS...")
    
    res_ec2 = ec2.describe_instances()
    total_instancias = sum(len(r['Instances']) for r in res_ec2['Reservations'])
    
    res_s3 = s3.list_buckets()
    total_buckets = len(res_s3['Buckets'])
    
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    reporte = f"""
    ==================================
    REPORTE DE INFRAESTRUCTURA DEVOPS
    Fecha: {fecha}
    ==================================
    Instancias EC2 activas: {total_instancias}
    Buckets S3 encont
rados: {total_buckets}
    ==================================
    """
    
    with open('reporte_infraestructura.txt', 'w') as archivo:
        archivo.write(reporte)
    
    print("✅ Reporte generado correctamente en 'reporte_infraestructura.txt'")

if __name__ == "__main__":
    generar_reporte()

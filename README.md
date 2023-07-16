# **ETL A LA API DEL BANCO DE MÉXICO** 💻🏦⭐

## **Método usado** 📡

En Python, se utiliza el método `request()` para hacer solicitudes a un servidor web y obtener respuestas. Toma varios parámetros, los más importantes son los siguientes:

- `method`: este parámetro especifica el método HTTP que se utilizará para la solicitud. Los métodos más comunes son GET, POST, PUT, DELETE, HEAD, OPTIONS, etc.

- `url`: este parámetro especifica la dirección URL del recurso que se va a solicitar.

- `params`: este parámetro es opcional y se utiliza para especificar los parámetros de la cadena de consulta de la URL.

- `data`: este parámetro es opcional y se utiliza para enviar datos en la solicitud, como formularios HTML o JSON.

- `headers`: este parámetro es opcional y se utiliza para enviar encabezados HTTP personalizados en la solicitud.

- `cookies`: este parámetro es opcional y se utiliza para enviar cookies en la solicitud.

- `auth`: este parámetro es opcional y se utiliza para enviar credenciales de autenticación en la solicitud.

- `timeout`: este parámetro es opcional y se utiliza para especificar el tiempo máximo de espera para la respuesta del servidor.

- `allow_redirects`: este parámetro es opcional y se utiliza para habilitar o deshabilitar la redirección automática de la solicitud.

Estos son algunos de los parámetros más comunes que se utilizan con la función `request()` de Python. Hay otros parámetros disponibles que se pueden utilizar según sea necesario para satisfacer requisitos específicos.

## **Información relevante:** 🔍

**Catálogo de series**
🔗 [Catálogo de series](https://www.banxico.org.mx/SieAPIRest/service/v1/doc/catalogoSeries)

**Formas de búsqueda:**
- GET series/:idSerie
- GET series/:idSerie/datos
- GET series/:idSerie/datos/oportuno
- GET series/:idSerie/datos/:fechaI/:fechaF


## **Series a descargar:** 📊

Datos del Banco de México.

Frecuencia diaria:
- Base monetaria pronosticada y observada:
    - Pronóstico SF44042 (miles de millones de pesos) 
    - Observado SF44043 (miles de millones de pesos).
    - Desviación SF44044 (miles de millones de pesos)

Frecuencia diaria:
- Base monetaria, circulante y depósitos:
    - Base monetaria SF43695 (millones de pesos)
    - Billetes y monedas en circulación SF43702 (millones de pesos)
    - Depósitos bancarios en cuenta corriente SF43696 (millones de pesos)

## **Información Adicional** ℹ️

### Códigos de estado HTTP:
- 200 OK: La solicitud se procesó correctamente y se devolvió una respuesta satisfactoria.
- 201 Created: La solicitud se ha completado y se ha creado un nuevo recurso como resultado.
- 204 No Content: La solicitud se ha completado correctamente, pero no hay contenido que devolver en la respuesta.
- 400 Bad Request: La solicitud no se pudo entender o se proporcionó información incorrecta.
- 401 Unauthorized: La solicitud requiere autenticación y el usuario no ha proporcionado credenciales válidas.
- 403 Forbidden: La solicitud se comprende, pero el servidor se niega a responder por razones legales o porque el usuario no tiene permisos para acceder al recurso solicitado.
- 404 Not Found: El recurso solicitado no se pudo encontrar en el servidor.
- 500 Internal Server Error: Se produjo un error en el servidor al procesar la solicitud.
- 502 Bad Gateway: El servidor actuando como gateway o proxy recibió una respuesta no válida del servidor ascendente.
- 503 Service Unavailable: El servidor está temporalmente fuera de servicio debido a una sobrecarga o mantenimiento del sistema.

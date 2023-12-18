Deploy ML Model untuk prediksi input teks fraud dengan FastAPI
## Cloud Computing

You can check the endpoints used for the machine learning models in this API. The available endpoints are `/predict_text` for text-based input and `/predict_image` for image-based input. 

For the `/predict_text` endpoint, you need to send a JSON payload with the following structure:
```json
{
  "text": "your text"
}
```

For the `/predict_image` endpoint, you need to send a multipart-form with a field named "uploaded_file" containing the image file.

You can view the API documentation by accessing the `/docs` endpoint after running the server. Additionally, a Dockerfile is provided to facilitate modification and container image creation. By default, the server runs on port 8080, but you can customize the port by injecting the `PORT` environment variable.

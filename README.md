
# Chat with Llama with Daytona

This repository contains a sample FastAPI application that leverages the Llama 3.2-Vision multimodal language model to generate image captions. It demonstrates seamless integration with Daytona for managing reproducible and secure development environments.

---

## 🚀 Getting Started

### Open Using Daytona

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).

2. **Create the Workspace**:  
   Clone this sample repository using Daytona:  
   ```bash
   daytona create https://github.com/sayantan007pal/Daytona-Authorizer
   ```

3. **Set Up Environment Variables**:  
   If your application requires environment variables, copy the example file and update it with your values:  
   ```bash
   cp .env.example .env
   ```  
   Ensure the following variables are set (if applicable):
   - `MODEL_NAME`: The name of the model to use (default is `Salesforce/blip-image-captioning-base`).
   - `DEVICE`: The device to run the model on (`cpu` or `cuda`).

4. **Install Dependencies**:  
   Inside the created workspace, install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:  
   Launch the application:  
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```  
   Your app should now be running at `http://localhost:8000`!

---

## ✨ Features

- **Image Captioning**: Upload images and receive AI-generated captions using the Llama 3.2-Vision model.
- **Multimodal AI**: Combines image and text processing for versatile use cases.
- **FastAPI Backend**: High-performance API built with FastAPI for handling requests efficiently.
- **Simple Frontend**: An intuitive HTML interface for easy interaction with the API.
- **Environment Management**: Utilizes Daytona for consistent and reproducible development environments.
- **Model Optimization**: Leverages LitServe for lightning-fast inference capabilities.

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🔗 Related Links

- **Daytona Documentation**: [https://github.com/daytonaio/daytona](https://github.com/daytonaio/daytona)
- **Llama 3.2-Vision Model**: [Hugging Face Model Page](https://huggingface.co/Salesforce/blip-image-captioning-base)
- **FastAPI Documentation**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **LitServe Documentation**: [LitServe GitHub](https://github.com/litserve/litserve)


## 📂 Project Directory Structure

```
Daytona-Authorizer/
├── .devcontainer/
│   └── devcontainer.json       # Defines the environment for Daytona
├── app/
│   ├── main.py                 # FastAPI application code
│   └── templates/
│       └── index.html           # HTML front-end for image uploads
├── .gitignore
├── README.md
├── requirements.txt           # List of Python dependencies
└── LICENSE                    # MIT License file
```

---

**Feel free to contribute or provide feedback! Happy coding! 🚀**
```

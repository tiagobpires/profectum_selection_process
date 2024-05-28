## Profectum Selection Process Challenge

This project is an REST API that connects with [Pipefy](https://www.pipefy.com/) to manage person-related cards. It fetches and validates card information, and provides a structured way to interact with Pipefy's GraphQL API.

### Features

- **Fetch Pipe Information**: Retrieve and display information about specific Pipefy pipes.
- **Manage Cards**: Create, update, and delete cards related to persons in Pipefy.
- **Field Validation**: Validate card fields according to Pipefy's field types and requirements.
- **API Documentation**: Swagger documentation available at `/docs/swagger/#/`.

### Tech Stack

- **Python**: The main programming language used for the API.
- **GraphQL**: Used for API connection with Pipefy.
- **Flask**: Web framework for creating the API.
- **Pydantic**: Data validation and settings management using Python type annotations.

### Installation

```sh
# Create a virtual environment (optional but recommended):
$ python -m venv venv

# Activate the virtual environment:
$ source venv/bin/activate

# Install requirements:
$ pip install -r requirements.txt
```

### Usage

Create a `.env` file and fill it with the information:

```sh
PIPE_ID=
PIPEFY_TOKEN=
```

To run, execute:

```sh
python main.py
```

Go to [http://localhost:5000/docs/swagger/#/](http://localhost:5000/docs/swagger/#/) to see the documentation.

### Fetching Pipe Information

Initially, it was necessary to retrieve information about the pipe, to know how the data is handled. The code for this is in the `initial_informations.py` file.

The response was:

```json
{
  "data": {
    "pipe": {
      "id": "<id>",
      "name": "Desafio - Vaga Profectum 2024.1",
      "phases": [
        {
          "id": "323403002",
          "name": "Caixa de entrada"
        },
        {
          "id": "323403003",
          "name": "Fazendo"
        },
        {
          "id": "323403004",
          "name": "Concluído"
        }
      ],
      "start_form_fields": [
        {
          "id": "nome",
          "label": "Nome",
          "type": "short_text",
          "required": true,
          "options": []
        },
        {
          "id": "data_de_nascimento",
          "label": "Data de nascimento",
          "type": "date",
          "required": false,
          "options": []
        },
        {
          "id": "cpf",
          "label": "CPF",
          "type": "cpf",
          "required": false,
          "options": []
        },
        {
          "id": "telefone",
          "label": "Telefone",
          "type": "phone",
          "required": false,
          "options": []
        },
        {
          "id": "data",
          "label": "Data de envio",
          "type": "datetime",
          "required": false,
          "options": []
        },
        {
          "id": "sexo",
          "label": "Sexo",
          "type": "radio_vertical",
          "required": false,
          "options": ["Masculino", "Feminino", "Prefere não responder"]
        },
        {
          "id": "hobbies",
          "label": "Hobbies",
          "type": "checklist_vertical",
          "required": false,
          "options": [
            "Teatro",
            "Música",
            "Cinema",
            "Esportes",
            "Leitura",
            "Viagem",
            "Artes"
          ]
        },
        {
          "id": "cidade",
          "label": "Cidade",
          "type": "connector",
          "required": true,
          "options": []
        }
      ]
    }
  }
}
```

The collected information was used along with the [field documentation](https://developers.pipefy.com/reference/fields#field-types) to create initial validation in the API.

# Tasks API

Petite API REST pédagogique construite avec Flask. Elle expose un contrôle de santé et des opérations de base sur une liste de tâches.

## Routes

| Méthode | Route | Résultat |
|---|---|---|
| GET | `/health` | État de l’API. |
| GET | `/tasks` | Tâches conservées en mémoire. |
| POST | `/tasks` | Crée une tâche depuis un titre JSON; retourne 201. |
| DELETE | `/tasks/{id}` | Supprime la tâche; retourne 204. |

Corps attendu par `POST /tasks` :

```json
{"title": "Préparer un entretien"}
```

## Lancer

Prérequis : Python 3.

```sh
python -m pip install -r requirements.txt
python src/app.py
```

L’API écoute sur le port 5000.

## Tests

```sh
python -m pytest
```

## Limites

Les tâches disparaissent à l’arrêt du processus. Le serveur Flask intégré sert au développement. L’API n’a ni authentification ni base de données; ne lui envoyez pas de données personnelles.

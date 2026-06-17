FROM python:3.9-slim

WORKDIR /app

RUN pip install flask joblib scikit-learn gunicorn
COPY app.py .
COPY iris_model.pkl .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

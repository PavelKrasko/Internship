FROM python:3.10-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl --fail http://localhost:5000/health || exit 1

USER appuser

CMD ["python", "app.py"]
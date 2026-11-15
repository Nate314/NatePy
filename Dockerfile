# syntax=docker/dockerfile:1
# Transpiles the README's example (Assignment2.npy) with natepy.py and runs the result,
# an interactive interest calculator that waits for input on the attached TTY.
FROM python:3.12-slim
WORKDIR /app
COPY natepy.py Assignment2.npy ./
CMD ["python", "natepy.py", "Assignment2.npy"]

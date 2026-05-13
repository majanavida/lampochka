# Лампочка

## Как запустить

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

После запуска откройте сайт в браузере:

```text
http://127.0.0.1:5000
```

## Как менять состояние лампочки

Включить лампочку:

```text
http://127.0.0.1:5000/button_on
```

Выключить лампочку:

```text
http://127.0.0.1:5000/button_off
```

## Как закрыть сайт

Вернитесь в терминал, где запущен `python app.py`, и нажмите:

```text
Ctrl+C
```

# Инструкция подключения к hadoop
- Переходим в папку `docker-hadoop`
- Сборка проекта: `docker-compose build`
- Запуск: `docker-compose up -d`
- Попасть в контейнер нодменеджера: `docker-compose exec nodemanager bash`
- Остановка: `docker-compose stop`
- Удаление: `docker-compose down -v`
- http://localhost:9870/ - информация о Hadoop кластере
- http://localhost:8088/ - менеджер ресурсов, отображающий выполняющиеся задачи

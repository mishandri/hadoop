# hadoop

1. Переходим в папку docker-hadoop
2. Сборка проекта: docker-compose build
3. Запуск: docker-compose up -d
4. Попасть в контейнер нодменеджера: docker-compose exec nodemanager bash
5. Остановка: docker-compose stop
6. Удаление: docker-compose down -v
7. http://localhost:9870/ - информация о Hadoop кластере
8. http://localhost:8088/ - менеджер ресурсов, отображающий выполняющиеся задачи

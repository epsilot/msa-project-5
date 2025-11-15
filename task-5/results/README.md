# Task 5

- Для мониторинга пакетной обработки имеет смысл использовать методику подбора метрик USE.
- В качестве Utilization можно использовать метрику Spring Boot Actuator spring_batch_job_seconds_count{spring_batch_job_name="importProductJob", spring_batch_job_status="COMPLETED"}.
- В качестве Saturation можно использовать метрику Spring Boot Actuator executor_queued_tasks.
- В качестве Errors можно использовать метрику Spring Boot Actuator spring_batch_job_seconds_count{spring_batch_job_name="importProductJob", spring_batch_job_status="FAILED"}.
- Методику четырёх сигналов или RED использовать видится не целесообразным для мониторга пакетной обработки из-за их
  ориентированности на систему предоставляющую API.
- Также имеет смысл дополнительно добавить метрики утилизации конкретных воркеров исполняющих задачи, а также информацию
  о времени выполнения однотипных задач.
- В качестве примера алёртинга настроено оповещение о ситуациях превышения количества задач, которые завершились ошибкой
  за определённый промежуток времени.

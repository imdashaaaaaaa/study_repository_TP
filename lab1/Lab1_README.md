## Цель работы: 
1. Создать репозиторий
2. Сделать коммит
3. Добавить удалённый репозиторий
4. Запушить локальные коммиты в удалённый репозиторий

# Создаем папку ТП по структуре: 
<img width="413" height="457" alt="image" src="https://github.com/user-attachments/assets/d94f268e-0678-41af-9a40-23dc5cad2a25" />

**git init** - для инициализации репозитория (создает в текущей директории гит-репозиторий (скрытую папку .git с базой данных и метаданными))

**git status** - просмотр, какой статус имеет каждый файл в проекте. 
Так как мы пока не добавляли файлы в индекс и не коммитили, их статус будет edited:

<img width="1266" height="762" alt="git status" src="https://github.com/user-attachments/assets/ec28a0aa-1c96-4b24-a71a-220f5fedd5ea" />

**git add .** - добавление всех файлов проекта в индекс, чтобы они были добавлены в будущий коммит (точка в конце обозначает добавление всех файлов)

**git config** - добавление информации о себе: имя и почта 
<img width="1266" height="762" alt="git status" src="https://github.com/user-attachments/assets/8aabed16-4131-48d5-af14-15ef1724a304" />

**git commit** - создание коммитов 

**git log** - просмотр истории коммитов в репозитории

## Создаем репозиторий в GitHub + уникальный SSH:
<img width="2738" height="1481" alt="repository" src="https://github.com/user-attachments/assets/aba668e2-1d1d-4a55-819a-7682ed5351da" />

**git remote** - добавление данных в локальный репозиторий об удаленном
<img width="2131" height="646" alt="remote" src="https://github.com/user-attachments/assets/51f509cb-16ba-422a-8188-745466f0ace0" />

**git push** - пуш в удаленный репозиторий

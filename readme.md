# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"

1. Какого типа команда `cd`? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.
   * Команда `cd` является встроенной в оболочку Bash командой и применяется для перемещения по директориям. 
2. Какая альтернатива без pipe команде `grep <some_string> <some_file> | wc -l`? `man grep` поможет в ответе на этот вопрос. Ознакомьтесь с [документом](http://www.smallo.ruhr.de/award.html) о других подобных некорректных вариантах использования pipe.
   * В качестве альтернативы связке команд `grep <some_string> <some_file> | wc -l` можно использовать `grep -с <some_string> <some_file>`. Ключ `-c` используется для подсчета строк с искомым шаблоном.
3. Какой процесс с PID `1` является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?
   * Процессом прородителем всех последующих процессов с PID `1` является процесс `Init`
4. Как будет выглядеть команда, которая перенаправит вывод stderr `ls` на другую сессию терминала?
   * Команда перенаправления `stderr` на другую сессию терминала может выглядеть следующим образом `ls asdf 2>&/dev/tty2`
5. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.
6. Получится ли находясь в графическом режиме, вывести данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?
7. Выполните команду `bash 5>&1`. К чему она приведет? Что будет, если вы выполните `echo netology > /proc/$$/fd/5`? Почему так происходит?
   * Команда `bash 5>&1` создает процесс `bash` с файловым дескриптором 5 и перенаправляет его в stdout. Таким образом выполнив затем команду `echo netology > /proc/$$/fd/5` мы сначала перенаправим вывод команды `echo` в файловый дескриптор 5, который в свою очередь уже перенаправлен в stdout
8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от `|` на stdin команды справа.
Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.
   * При помощи Можно направить `stderr` коман 
9. Что выведет команда `cat /proc/$$/environ`? Как еще можно получить аналогичный по содержанию вывод?
   * Команда `cat /proc/$$/environ` выводит список переменных окружения. Такой же результат можно получить командой `printenv`
10. Используя `man`, опишите что доступно по адресам `/proc/<PID>/cmdline`, `/proc/<PID>/exe`.
    * По адресу `/proc/<PID>/cmdlite` находится команда выполняющейся в данный момент программа, в то время как `/proc/<PID>/exe` является символической ссылкой на саму это программу.
11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью `/proc/cpuinfo`.
    * Командой `grep sse /proc/cpuinfo` можно узнать, что самой старшей версией набора инструкций SSE на моем процессоре является SSE4_2.
12. При открытии нового окна терминала и `vagrant ssh` создается новая сессия и выделяется pty. Это можно подтвердить командой `tty`, которая упоминалась в лекции 3.2. Однако:

     ```bash
     vagrant@netology1:~$ ssh localhost 'tty'
     not a tty
     ```

     Почитайте, почему так происходит, и как изменить поведение.
    * 
13. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись `reptyr`. Например, так можно перенести в `screen` процесс, который вы запустили по ошибке в обычной SSH-сессии.
    * Я указанном примере я использовал команду `htop` и следующую последовательность действий:
      1. Запустил `htop`
      2. Командой `disown htop` отсоединил от своей сессии.
      3. Переключился в другой терминал
      4. Командой `ps ax` выяснил PID процесса `htop`
      5. Переключил `htop` в свой новый терминал командой `reptyr <PID>`
14. `sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без `sudo` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию `echo string | sudo tee /root/new_file`. Узнайте что делает команда `tee` и почему в отличие от `sudo echo` команда с `sudo tee` будет работать.
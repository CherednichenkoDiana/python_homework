from time import sleep

class User:
    def __init__(self, nickname, password , age):
        self.nickname = nickname
        self.password = password #password - hash?!
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        elif isinstance(other, str):
            return self.nickname == other

    def __lt__(self, other):
        if isinstance(other, int):
            return self.age < other
        elif isinstance(other, User):
            return self.age < other.age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.title == other.title
        elif isinstance(other, str):
            return self.title == other

    def __contains__(self, item):
        return item.upper() in self.title.upper()

class UrTube:
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        log_user = None
        for user in self.users:
            if user == nickname and user.password == password:
                log_user = user
        if log_user != None:
            self.current_user = log_user


    def register(self, nickname, password, age):
        flag_name = False
        for name in self.users:
            if name == nickname:
                flag_name = True
        if flag_name:
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname,password,age)
            self.users.append(new_user)
            self.log_in(nickname,password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for v in video:
            self.videos.append(v)

    def get_videos(self,search):
        res = []
        for v in self.videos:
            if search in v:
                res.append(v.title)
        return res

    def watch_video(self, video_title):
        watch_film = None
        if self.current_user != None:
            for v in self.videos:
                if video_title == v:
                    watch_film = v
            if watch_film != None:
                if watch_film.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    while watch_film.time_now < watch_film.duration:
                        watch_film.time_now += 1
                        sleep(1)
                        print(watch_film.time_now, end=' ')
                    watch_film.time_now = 0
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 3, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
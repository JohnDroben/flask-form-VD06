from flask import render_template, request, redirect, url_for, flash
from app import app

# Временное хранилище данных (в реальном приложении используйте БД)
users_data = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Простая валидация
        if not all([name, city, hobby, age]):
            flash('Все поля обязательны для заполнения!', 'danger')
            return redirect(url_for('index'))

        try:
            age = int(age)
        except ValueError:
            flash('Возраст должен быть числом!', 'danger')
            return redirect(url_for('index'))

        users_data.append({
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        })

        flash('Анкета успешно сохранена!', 'success')
        return redirect(url_for('index'))

    return render_template('blog.html', users=users_data)
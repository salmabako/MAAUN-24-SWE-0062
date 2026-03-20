from flask import Flask, render_template, request, redirect, url_for
from models import Business, Directory

app = Flask(__name__)

kubwa_hub = Directory()

sample_biz = Business("Kubwa Fresh Farms", "Agriculture", "Locally sourced hydroponic vegetables.")
kubwa_hub.add_business(sample_biz)

@app.route('/')
def home():
    """Route 1: Displays the Stack of recently added businesses."""
    recent_businesses = kubwa_hub.get_recent_businesses()
    return render_template('index.html', businesses=recent_businesses)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    """Route 2: Displays the form and handles adding to the Stack."""
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')

        new_biz = Business(name, category, description)
        kubwa_hub.add_business(new_biz)

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/edit/<biz_id>', methods=['GET', 'POST'])
def edit_business(biz_id):
    """Route 3: Handles editing an existing business."""
    biz = kubwa_hub.get_business_by_id(biz_id)

    if not biz:
        return redirect(url_for('home'))

    if request.method == 'POST':
        updated_name = request.form.get('name')
        updated_category = request.form.get('category')
        updated_desc = request.form.get('description')

        biz.update_details(updated_name, updated_category, updated_desc)

        return redirect(url_for('home'))

    return render_template('edit.html', biz=biz)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

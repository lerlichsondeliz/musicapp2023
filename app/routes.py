from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewArtistForm

artists_data = [
    {
        'id': 1,
        'name': "INABAKUMORI",
        'songs': "Lost Umbrella, Lagtrain, Hello Marina, Anticyclone, Pascal Beats, Loop Spinner",
        'general_info': "Inabakumori is a Vocaloid producer",
    },
    {
        'id': 2,
        'name': "Gunpoets",
        'songs': "Song 3, Song 4",
        'general_info': "Hip-hop group from Ithaca",
    },
    {
        'id': 3,
        'name': "Donna The Buffalo",
        'songs': "Song 5, Song 6",
        'general_info': "Folk-rock band from Ithaca",
    },
    {
        'id': 4,
        'name': "The Blind Spots",
        'songs': "Song 7, Song 8",
        'general_info': "Indie rock band from Ithaca",
    },

]
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome to Ithaca Music')


@app.route('/artists', methods=['GET', 'POST'])
def artists():

    return render_template('artists.html', title='List of Ithaca Artists', artists=artists_data)


@app.route('/new_artists', methods=['GET', 'POST'])
def new_artists():
    form = NewArtistForm()
    if form.validate_on_submit():
        flash('Artist added successfully', 'success')
        return redirect(url_for('new_artists'))

    return render_template('new_artists.html', title='New Artists', form=form)


@app.route('/artist/<int:artist_id>')
def artist(artist_id):
    artist_data = next((artist for artist in artists_data if artist['id'] == artist_id), None)

    if artist_data is None:
        flash('Artist not found', 'danger')
        return redirect(url_for('artists'))

    return render_template('artist.html', title='Artist Details', artist=artist_data)

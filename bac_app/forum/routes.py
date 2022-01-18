from . import views

def setup_router(app):
    app.router.add_get('/', views.index)
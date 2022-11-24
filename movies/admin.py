from django.contrib import admin

from movies.models import Role, Genre, Movie, MovieCrew, Crew, MovieComment, MovieRate


# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('is_valid', )


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    extra = 2


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'is_valid')
    search_fields = ('title', )
    list_filter = ('is_valid', )
    inlines = (MovieCrewInline, )


class CrewAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'is_valid')
    search_fields = ('first_name', 'last_name', 'gender')
    list_filter = ('is_valid', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_body', 'status')


class Rate(admin.ModelAdmin):
    list_display = ('rate',)


admin.site.register(Role, RoleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(MovieComment, CommentAdmin)
admin.site.register(MovieRate, Rate)

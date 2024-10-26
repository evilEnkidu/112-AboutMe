# Mini Challenge 1

## Your about page

### Acceptance Criteria
1. Create a view that extends `TemplateView` in `pages/views.py`
1.1. The new view should be named `AboutPageView` for this exercise.
1.2. The template_name attribute should be set to `pages/about.html`
2. Create a urlpattern in `pages/urls.py` that maps `about/` to `AboutPageView.as_view()`
2.1. The name tag or label associated with this new urlpattern should be `about`
3. Populate the template `pages/about.html`
3.1. This should contain a short blurb or bio about yourself, the developer of this site.

## Bonus
Research how to add an image from `static/img` and have it displayed on your about template.
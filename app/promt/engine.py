from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("app/prompt/templates"))

def render_prompt(name, **kwargs):
    return env.get_template(name).render(**kwargs)

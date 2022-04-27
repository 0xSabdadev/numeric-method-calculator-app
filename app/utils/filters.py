from app import app

@app.template_filter("to_id")
def to_id_filter(group_name):
    group_name = group_name.split(" ")
    group_name = group_name[0] + group_name[1].capitalize()
    return group_name

app.jinja_env.filters["to_id"] = to_id_filter

@app.template_filter("to_url")
def to_url_filter(member_name):
    member_name = member_name.replace(" ", "-")
    member_name = member_name.replace("/", "-")
    return member_name

app.jinja_env.filters["to_url"] = to_url_filter
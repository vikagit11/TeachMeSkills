from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import Poll, Option
from .forms import PollForm

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    polls = Poll.query.all()
    return render_template("index.html", polls=polls)

@bp.route("/poll/<int:poll_id>", methods=["GET", "POST"])
def poll_detail(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    if request.method == "POST":
        option_id = request.form.get("option")
        option = Option.query.get(option_id)
        option.votes += 1
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("poll_detail.html", poll=poll)

@bp.route("/create", methods=["GET", "POST"])
def create_poll():
    form = PollForm()

    print("Submitted:", form.is_submitted())
    print("Valid:", form.validate())
    print("Errors:", form.errors)

    if request.method == "POST":
        poll = Poll(question=form.question.data)
        db.session.add(poll)
        db.session.flush()
        for opt_form in form.options:
            db.session.add(Option(text=opt_form.text.data, poll_id=poll.id))
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("create_poll.html", form=form)

@bp.route("/delete/<int:poll_id>", methods=["POST"])
def delete_poll(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    db.session.delete(poll)
    db.session.commit()
    return redirect(url_for("main.index"))

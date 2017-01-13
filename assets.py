from flask.ext.assets import Bundle, Environment
from app import app

bundles = {

    'js': Bundle(
        "static/bootstrap.js",
        "static/jquery.js",

    )
    'css': Bundle(
        "static/bootstrap.css",
        "static/2-col-portfolio.css"
    )

    'img': Bundle(
        "static/dreamSequence2.jpg",
        "static/dreamSequenceRB.jpg",
        "static/RB5leaves.jpg",
        "static/RBbranchDancenew.jpg",
        "static/RBpurpyellow1.jpg",

    )

}

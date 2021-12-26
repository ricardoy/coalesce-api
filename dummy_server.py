from flask import Flask, jsonify

app = Flask("dummy server")


@app.route("/api1/<int:member_id>", methods=["GET"])
def api1(member_id: int):
    return jsonify(
        {
            "deductible": member_id * 100,
            "stop_loss": member_id * 100,
            "oop_max": member_id * 100,
        }
    )


@app.route("/api2/otherpath/<int:member_id>", methods=["GET"])
def api2(member_id: int):
    return jsonify(
        {
            "deductible": member_id * 200,
            "stop_loss": member_id * 200,
            "oop_max": member_id * 200,
        }
    )


@app.route("/api3/another/path/<int:member_id>", methods=["POST"])
def api3(member_id: int):
    return jsonify(
        {
            "deductible": member_id * 300,
            "stop_loss": member_id * 300,
            "oop_max": member_id * 300,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

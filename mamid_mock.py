from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html', title="Dashboard", crumb=[], poverview=True)


@app.route('/slaves')
def hosts():
    slaves = []
    disabled = []
    for i in range(12, 62):
        slaves.append("mksuns{}".format(i))
    for i in range(62, 67):
        disabled.append("mksuns{}".format(i))
    return render_template('slaves.html', title="Hosts", slaves=slaves, disabled=disabled,
                           crumb=[{'name': 'Slaves', 'url': '/slaves'}],
                           pslaves=True)


@app.route('/replicasets')
def replicat_sets():
    return render_template('replica_sets.html', title="Replica Sets",
                           crumb=[{'name': 'Replica Sets', 'url': '/replicasets'}], preplicasets=True)


@app.route('/problems')
def problems():
    return render_template('problems.html', title="Problems", crumb=[{'name': 'Problems', 'url': '/problems'}],
                           pproblems=True)


@app.route('/riskgroups')
def riskgroups():
    cabB = []
    cabA = []
    unused = []
    for i in range(12, 30):
        cabB.append("mksuns{}".format(i))

    for i in range(30, 40):
        cabA.append("mksuns{}".format(i))

    for i in range(62, 67):
        unused.append("mksuns{}".format(i))
    return render_template('risk_groups.html', title="Risk Groups",
                           crumb=[{'name': 'Risk Groups', 'url': '/riskgroups'}], priskgroups=True, cabB=cabB,
                           cabA=cabA, unused=unused)


@app.route('/new/slave')
def new_host():
    return render_template('edit_slave.html', title="New Slave", pnewslave=True,
                           crumb=[{'name': 'New Slave', 'url': '/new/slave'}])


@app.route('/new/replicaset')
def new_replica_set():
    return render_template('edit_replicaset.html', title="New Replica Set", pnewreplicaset=True,
                           crumb=[{'name': 'New Replica Set', 'url': '/new/replicaset'}])


@app.route('/slave/<slave>/edit/<mockupstate>')
def edit_slave(slave, mockupstate):
    return render_template('edit_slave.html', slavename=slave, title="Slave '{}'".format(slave),
                           crumb=[{'name': 'Slaves', 'url': '/slaves'},
                                  {'name': slave, 'url': '/slave/{}/edit/{}'.format(slave, mockupstate)}], pslaves=True,
                           state=mockupstate)


@app.route('/replicaset/<replicaset>/edit/<state>')
def edit_replica_set(replicaset, state):
    return render_template('edit_replicaset.html', slavename=replicaset, title="Replica Set '{}'".format(replicaset),
                           crumb=[{'name': 'Replica Sets', 'url': '/replicasets'},
                                  {'name': replicaset, 'url': '/rpelicaset/{}/edit/{}'.format(replicaset, state)}],
                           preplicasets=True,
                           state=state)


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)

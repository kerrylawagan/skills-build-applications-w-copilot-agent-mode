function App() {
  return (
    <Router>
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
          <Link className="navbar-brand text-white" to="/">Octofit Tracker</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item"><Link className="nav-link text-white" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card mt-4">
              <div className="card-body">
                <h1 className="card-title text-center">Welcome to Octofit Tracker!</h1>
                <p className="card-text text-center">Track your fitness activities, join teams, and compete on the leaderboard.</p>
                <div className="text-center">
                  <Link to="/activities" className="btn btn-success m-2">View Activities</Link>
                  <Link to="/leaderboard" className="btn btn-info m-2">Leaderboard</Link>
                  <Link to="/teams" className="btn btn-warning m-2">Teams</Link>
                  <Link to="/users" className="btn btn-primary m-2">Users</Link>
                  <Link to="/workouts" className="btn btn-secondary m-2">Workouts</Link>
                </div>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

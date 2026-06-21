import { useState } from "react";
import axios from "axios";
import CandidateModal from "../components/CandidateModal";
import CompareModal from "../components/CompareModal";

function Dashboard() {

    const [jd, setJd] = useState(null);
    const [resumes, setResumes] = useState([]);
    const [results, setResults] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [selectedCandidate, setSelectedCandidate] = useState(null);
    const [compareCandidates, setCompareCandidates] = useState([]);
    const [showComparision,setShowComparision] = useState(false);

    const addToCompare = (candidate) => {
        const exists = compareCandidates.some(
        c => c.candidate_name === candidate.candidate_name
    );

    if (exists) {
        alert("Candidate already selected");
        return;
    }

    if (compareCandidates.length >= 2) {
        alert("Only 2 candidates can be compared");
        return;
    }

    setCompareCandidates([
        ...compareCandidates,
        candidate
    ]);
    };

    const rankCandidates = async () => {

        const formData = new FormData();

        formData.append("jd", jd);

        for (let file of resumes) {
          formData.append("resumes", file);
        }

        const response = await axios.post(
          "http://localhost:8000/rank-candidates",
          formData
        );

        setResults(response.data);

    };

    return (

        <div className="container mt-5">

      <h2>AI Resume Screening Dashboard</h2>

      <div className="mb-3">

        <label>Upload Job Description</label>

        <input
          type="file"
          className="form-control"
          onChange={(e) => setJd(e.target.files[0])}
        />

      </div>

      <div className="mb-3">

        <label>Upload Resumes</label>

        <input
          type="file"
          multiple
          className="form-control"
          onChange={(e) => setResumes([...e.target.files])}
        />

      </div>

      <button
        className="btn btn-primary"
        onClick={rankCandidates}
      >
        Rank Candidates
      </button>

      <hr />

      <table className="table table-bordered">

        <thead>
          <tr>
            <th>Rank</th>
            <th>Candidate</th>
            <th>Score</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {results.map((candidate, index) => (

            <tr key={index}>

              <td>{index + 1}</td>

              <td>
                {candidate.candidate_name ||
                 candidate.filename}
              </td>

              <td>{candidate.score}</td>

              <td>{candidate.recommendation}</td>

              <td>
                  <button
                      className="btn btn-success btn-sm"
                      onClick={() => {
                          setSelectedCandidate(candidate);
                          setShowModal(true);
                      }}
                  >
                      View Details
                  </button>



                  <button
                      className="btn btn-success btn-sm ms-2"
                      onClick={() => addToCompare(candidate)}
                  >
                     Compare
                  </button>
              </td>

            </tr>

          ))}

        </tbody>

      </table>

      {
  compareCandidates.length === 2 && (

    <button
      className="btn btn-warning mt-3"
      onClick={() => setShowComparision(true)}
    >
      Compare Candidates
    </button>

  )
}



      <CandidateModal
          show = {showModal}
          handleClose={() => setShowModal(false)}
          candidate={selectedCandidate}
      />

      <CompareModal
    show={showComparision}
    handleClose={() =>
        setShowComparision(false)
    }
    candidates={compareCandidates}
/>


    </div>

    );
}



export default Dashboard;
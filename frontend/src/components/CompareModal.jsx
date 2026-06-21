import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

function CompareModal({
    show,
    handleClose,
    candidates
}) {

    if (!candidates || candidates.length < 2)
        return null;

    const c1 = candidates[0];
    const c2 = candidates[1];

    return (

        <Modal
            show={show}
            onHide={handleClose}
            size="xl"
        >

            <Modal.Header closeButton>

                <Modal.Title>
                    Candidate Comparison
                </Modal.Title>

            </Modal.Header>

            <Modal.Body>

                <table className="table">

                    <thead>

                        <tr>
                            <th>Metric</th>
                            <th>{c1.candidate_name}</th>
                            <th>{c2.candidate_name}</th>
                        </tr>

                    </thead>

                    <tbody>

                        <tr>
                            <td>Score</td>
                            <td>{c1.score}</td>
                            <td>{c2.score}</td>
                        </tr>

                        <tr>
                            <td>Recommendation</td>
                            <td>{c1.recommendation}</td>
                            <td>{c2.recommendation}</td>
                        </tr>

                        <tr>
                            <td>Strengths</td>
                            <td>{c1.strengths?.join(", ")}</td>
                            <td>{c2.strengths?.join(", ")}</td>
                        </tr>

                        <tr>
                            <td>Missing Skills</td>
                            <td>{c1.missing_skills?.join(", ")}</td>
                            <td>{c2.missing_skills?.join(", ")}</td>
                        </tr>

                    </tbody>

                </table>

                <h4 className="mt-3">

                    Winner: {

                        c1.score > c2.score
                        ? c1.candidate_name
                        : c2.candidate_name

                    }

                </h4>

            </Modal.Body>

            <Modal.Footer>

                <Button
                    variant="secondary"
                    onClick={handleClose}
                >
                    Close
                </Button>

            </Modal.Footer>

        </Modal>
    );
}

export default CompareModal;
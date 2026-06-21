import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

function CandidateModal({
    show,
    handleClose,
    candidate
}) {

    if (!candidate) return null;

    return (
        <Modal
            show={show}
            onHide={handleClose}
            size="lg"
        >

            <Modal.Header closeButton>
                <Modal.Title>
                    {candidate.candidate_name}
                </Modal.Title>
            </Modal.Header>

            <Modal.Body>

                <h5>
                    Score: {candidate.score}
                </h5>

                <h5>
                    Recommendation:
                    {" "}
                    {candidate.recommendation}
                </h5>

                <hr />

                <h5>Strengths</h5>

                <ul>
                    {candidate.strengths?.map(
                        (item, index) => (
                            <li key={index}>
                                {item}
                            </li>
                        )
                    )}
                </ul>

                <h5>Missing Skills</h5>

                <ul>
                    {candidate.missing_skills?.map(
                        (item, index) => (
                            <li key={index}>
                                {item}
                            </li>
                        )
                    )}
                </ul>

                <h5>Interview Questions</h5>

                <ol>
                    {candidate.interview_questions?.map(
                        (item, index) => (
                            <li key={index}>
                                {item}
                            </li>
                        )
                    )}
                </ol>

                <h5>Summary</h5>

                <p>
                    {candidate.summary}
                </p>

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

export default CandidateModal;

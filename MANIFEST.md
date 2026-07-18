# Release manifest

The five supplied analysis notebooks were renamed into a numbered,
descriptive sequence. Notebook outputs and execution counters were removed
to avoid publishing stale cached results, and dependency installation was
moved to `requirements.txt`.

The release parameter constants were aligned with the revised manuscript:
`σ_PI=0.02` for timing jitter and ramp distortion, and `σ_PI=0.005` for OU,
ripple, and combined perturbations. No other numerical algorithm or
classification logic was changed.

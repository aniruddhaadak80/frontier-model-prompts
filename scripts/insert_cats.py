"""Insert 3 new categories into generate_prompts.py before the closing bracket."""
from pathlib import Path
p = Path("scripts/generate_prompts.py")
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
# find index of the line that is just ']' followed (eventually) by PER_CATEGORY
target = None
for i, l in enumerate(lines):
    if l.strip() == "]":
        # check if PER_CATEGORY follows within next few lines
        for j in range(i+1, min(i+6, len(lines))):
            if "PER_CATEGORY" in lines[j]:
                target = i
                break
        if target is not None:
            break
assert target is not None, "closing bracket not found"
new_block = '''    dict(slug="32-robotics", emoji="🤖", title="Robotics & Embodied AI",
         desc="Perception, planning, control, sim-to-real, and safety for embodied agents.",
         roles=["senior robotics engineer", "expert perception researcher", "senior motion-planning engineer", "expert control systems engineer", "senior sim-to-real lead", "expert HRI designer"],
         tasks=["design a perception pipeline for object detection and tracking", "build a motion planner with collision avoidance", "create a sim-to-real transfer plan for a manipulator", "design a grasp planner with force feedback", "build a SLAM pipeline with loop closure", "create a safety envelope for a mobile robot", "design a teleoperation interface with haptics", "build a dataset collection plan for imitation learning", "create a behavior tree for a service robot", "design a navigation stack for indoor environments", "build a calibration procedure for sensors", "create a failure-recovery plan for manipulation", "design a multi-robot coordination protocol", "build an evaluation harness for embodied tasks", "create a human-robot interaction study plan"],
         audiences=["for a research lab", "for a startup", "for an industrial robot", "for a service robot", "for a classroom", "for a hackathon"],
         constraints=["safety first: estop, limits, and monitoring", "validate in sim before hardware", "log telemetry for every run", "respect workspace and force limits", "test edge cases and failure modes", "document assumptions and sensor limits"],
         outputs=["an architecture spec", "a control design", "a sim-to-real plan", "a safety checklist", "an eval harness", "a deployment runbook"]),
    dict(slug="33-finance-quant", emoji="💰", title="Finance & Quantitative Analysis",
         desc="Pricing, risk, portfolios, and market analysis with rigorous assumptions.",
         roles=["senior quant analyst", "expert risk modeler", "senior portfolio manager aide", "expert fintech engineer", "senior compliance analyst", "expert data scientist (finance)"],
         tasks=["build a Black-Scholes pricer with Greeks", "design a portfolio optimization with constraints", "create a VaR/CVaR risk model", "build a backtesting harness with slippage", "design a factor model with validation", "create a fraud-detection feature set", "build a credit-scoring model card", "design a market-making simulator", "create a rebalancing policy with costs", "build a stress-test scenario set", "design a P&L attribution report", "create a liquidity-risk monitor", "build an options strategy backtest", "design a KYC/AML screening flow", "create a regulatory capital report"],
         audiences=["for a hedge fund", "for a bank", "for a fintech startup", "for a regulator", "for a classroom", "for a researcher"],
         constraints=["state assumptions and model limits", "no investment advice; analysis only", "validate on out-of-sample data", "document data sources and biases", "respect regulatory constraints", "include stress tests and edge cases"],
         outputs=["a model spec", "a risk report", "a backtest summary", "a compliance checklist", "a dashboard spec", "a validation report"]),
    dict(slug="34-legal-compliance", emoji="⚖️", title="Legal & Compliance",
         desc="Contracts, policy, privacy, and regulatory workflows with careful sourcing.",
         roles=["senior legal analyst", "expert privacy counsel aide", "senior compliance officer", "expert contract reviewer", "senior policy writer", "expert audit lead"],
         tasks=["draft a privacy policy with data flows", "build a contract review checklist", "create a GDPR compliance gap analysis", "design a terms-of-service with edge cases", "build a data-retention schedule", "create an incident-response legal plan", "design an IP assignment agreement outline", "build a vendor-risk assessment", "create a regulatory change tracker", "design an ethics review rubric", "build a consent-management flow", "create a license-compliance audit", "design a whistleblower policy", "build a board-reporting template", "create a litigation-hold checklist"],
         audiences=["for a startup", "for an enterprise", "for a nonprofit", "for a healthcare org", "for a school", "for a regulator"],
         constraints=["not legal advice; for review only", "cite regulations and sources", "flag jurisdiction-specific items", "protect privileged/PII data", "require human review for filings", "version and date all docs"],
         outputs=["a policy draft", "a compliance checklist", "a gap analysis", "a contract outline", "an audit plan", "a reporting template"]),
'''
# insert new_block before target line (the ']' line), preserving its newline
lines.insert(target, new_block)
p.write_text("".join(lines), encoding="utf-8")
print("inserted before line", target+1)
"
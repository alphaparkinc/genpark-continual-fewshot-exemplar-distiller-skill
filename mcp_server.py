import json, sys
from client import ContinualFewshotExemplarDistillerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "continual-fewshot-exemplar-distiller", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "distill_fewshot_exemplars", "description": "Mines historical agent trajectories and distills high-performing few-shot prompt exemplars."}]}}
    elif method == "tools/call":
        client = ContinualFewshotExemplarDistillerClient()
        res = client.distill_fewshot_exemplars()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = ContinualFewshotExemplarDistillerClient()
        print(json.dumps(client.distill_fewshot_exemplars(), indent=2))

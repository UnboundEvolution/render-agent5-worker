import time

def run():
    print("Agent 5 Render Worker ready...")
    while True:
        print("Waiting for webhook trigger...")
        time.sleep(60)

if __name__ == "__main__":
    run()

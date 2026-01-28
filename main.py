from dotenv import load_dotenv
from goc_api import GolemioClient
from visualizer import Visualizer

def main():
    load_dotenv()
    client = GolemioClient()
    Visual = Visualizer()

    # Šumavská
    print(Visual.visualize_departure_board(client.get_departure_boards("U744Z1P", limit=5)))

    # Vinohradská tržnice
    print(Visual.visualize_departure_board(client.get_departure_boards("U850Z1P", limit=5)))


if __name__ == "__main__":
    main()
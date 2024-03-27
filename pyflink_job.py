from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from pyflink.common import Configuration

def simple_flink_job():
    # Create a Configuration object
    config = Configuration()
    config.set_string("jobmanager.rpc.address", "localhost")
    config.set_string("jobmanager.rpc.port", "6123")
    # config.set_string("python.executable", "/usr/bin/python3")  # Adjust the path as needed
    print('set up config')

    # Create a StreamExecutionEnvironment with the configuration
    env = StreamExecutionEnvironment.get_execution_environment(config)
    print('set up env')
    

    # Set parallelism to 1 for easy viewing
    env.set_parallelism(1)
    print('set up parallelism')

    # Create some sample data
    data = [1, 2, 3, 4, 5]

    # Create a DataStream from the sample data
    data_stream = env.from_collection(collection=data, type_info=Types.INT())
    print('set up data stream')

    # Apply a simple transformation (e.g., multiply each number by 2)
    transformed_stream = data_stream.map(lambda x: x * 2, output_type=Types.INT())
    print('transformed stream')

    # Print the results to the console
    transformed_stream.print()
    print('print tranformed stream')

    # Execute the Flink job
    env.execute("Simple Flink Job")

    print('done executing')

if __name__ == "__main__":
    simple_flink_job()

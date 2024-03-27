from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types

# Initialize the StreamExecutionEnvironment
env = StreamExecutionEnvironment.get_execution_environment()

# Generate a stream that emits the result of 1 + 2
result_stream = env.from_collection([1], Types.INT()) \
    .map(lambda value: value + 2, output_type=Types.INT()) \
    .map(lambda value: str(value), output_type=Types.STRING()) \
    .map(lambda value: bytes(value, 'utf-8'), output_type=Types.BYTES()) \
    .sink_to_socket('localhost', 9000, SimpleStringEncoder())

# Execute the job
env.execute("Addition Job")

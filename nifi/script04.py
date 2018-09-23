import json
import sys
import traceback
import datetime
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil


class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_obj = json.loads(input_text)

            # Transform content
            output_arr = []
            start_time = input_obj['start_time']
            end_time = input_obj['end_time']
            id = input_obj['id']
            meas_type = input_obj['meas_type']

            date = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            endtime = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

            while date < endtime:
                output_obj = {
                    "id": id,
                    "meas_type": meas_type,
                    "val": 0,
                    "create_time": date.strftime("%Y-%m-%d %H:%M:%S"),
                    "create_day": datetime.datetime.strptime(date.strftime("%Y-%m-%d"), '%Y-%m-%d').strftime(
                        "%Y-%m-%d %H:%M:%S"),
                    "create_minute": date.strftime("%H:%M:%S")
                }
                if date.strftime("%M") == "00":
                    output_obj['vtype'] = '时间'
                elif date.strftime("%M") == "01":
                    output_obj['vtype'] = '最大值'
                elif date.strftime("%M") == "02":
                    output_obj['vtype'] = '最小值'
                else:
                    output_obj['vtype'] = '平均值'
                date = date + datetime.timedelta(minutes=1)
                print(output_obj)
                # Write output content
                output_arr.append(output_obj)
            output_text = json.dumps(output_arr)
            outputStream.write(StringUtil.toBytes(output_text))

        except:
            traceback.print_exc(file=sys.stdout)
            raise


#flowFile = session.create()
flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())
    # Finish by transferring the FlowFile to an output relationship
    session.transfer(flowFile, REL_SUCCESS)

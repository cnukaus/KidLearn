paths_points = [i for i in list(cj_df.path.str.split(" > ").values)]

    def _check_valid_touchpoints(paths_points):
        invalid_touchpoints = ["CONVERSION", "null", ""]
        counter = 0
        for path in paths_points:
            counter += 1
            for touchpoint in path:
                if touchpoint.isspace() or touchpoint in invalid_touchpoints:
                    raise ValueError(f"Path {counter} {path} has invalid blank touchpoint.")

# ws's way to init class variables
    @property
    def fbaa_table(self):
        """Getter for new_fbaa_table"""
        return self.new_fbaa_table
    
    @fbaa_table.setter
    def fbaa_table(self, value)
        """setter :D"""
        self.new_fbaa_table = value

#class Class:
# ...
#instance = Class()
#instance.fbaa_table=3
#
187949569816965
    result_id = obj_ins.executeTemplate(
        template_touchpoints,
        ast.literal_eval(macro_value_json),
    )
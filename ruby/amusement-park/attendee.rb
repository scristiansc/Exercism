class Attendee
  def initialize(height)
    @height = height
    @pass_id = nil
  end

  def height
    @height
  end

  def pass_id
    @pass_id
  end

  def issue_pass!(new_pass_id)
    @pass_id = new_pass_id
  end

  def revoke_pass!
    @pass_id = nil
  end
end
